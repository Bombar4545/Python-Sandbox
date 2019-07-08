/**
 * Author: Ufuk Bombar
 * Date: Jul 6 2019
 */

#ifndef __GAME_HPP
#define __GAME_HPP

// Includes
#include <vector>
#include <map>
#include <SFML/Graphics.hpp>

// Represents the dimension of a view frame in terms of no. of cells.
#define VIEW_FRAME_DIMENSION_CELL_WIDTH 32
#define VIEW_FRAME_DIMENSION_CELL_HEIGHT 18

// Window title
#define WINDOW_TITLE "Game of Life"

// Pixel size of each cell.
#define CELL_SIZE_PIXEL 15

// Rules for cell life.
// 0 : Cell will die
// 1 : Cell will continue to live
// 2 : A new cell will born
// adjacent cells : 0  1  2  3  4  5  6  7  8
#define CELL_RULES 0, 0, 1, 2, 0, 0, 0, 0, 0

class Chunk;
class GameOfLife;
struct Vector2l;

// Chunk size represents an edge of a chunk. There are CHUNK_WIDTH^2 cells in each 
// chunk.
#define CHUNK_WIDTH 16

/**
* Vector2l is copmosed of two longs that represents x and y coordinates in cartesian 
* coordinate system.
* 
* Some cases it can also represent width and height. Initial values are 0 to 0.
*/
struct Vector2l
{
    /**
     * Basic constructor.
     */
    Vector2l(long x, long y);

    /**
     * This function is necessary for hashing.
     */
    bool operator<(const Vector2l& vec) const;

    long x = 0;
    long y = 0;
};

/**
 * Chunk is a set of Cells that are computable by one thread. Each Chunk is responsible
 * for its own update and memory.
 */
class Chunk
{
    public:
        /**
         * Cell is a composition of Vector2l and bool which represents alive or not.
         */
        struct Cell
        {
            Vector2l pos;
            bool alive = false;
        };

        /**
         * Initializes the chunk variables: 'activelist', 'renderlist', 'position'.
         */
        Chunk(const Vector2l& pos);

        /**
         * Takes instance of GameOfLife class for getting adjacent chunks & rule info.
         * Updates the chunk by the following procedure:
         * 
         * Checks the status for all active cells:
         * 
         * When a cell is born all adjacent cells are added into the active list.
         * 
         * When a cell dies all adjacent are checked for any living neigbor. If not they
         * also got removed from the active list also.
         */
        void update(GameOfLife& game);

        /**
         * Takes x and t position returns if the corresponding cell is alive or not
         */
        bool isAlive(const Vector2l& pos);

    private:
        std::vector<Cell> activelist;

        // Render list is row oriented.
        bool renderlist[CHUNK_WIDTH][CHUNK_WIDTH];

        Vector2l position;

        /**
         * Clears the render list, initializes each cell to dead for fresh start.
         */
        void clearRenderList();

};

/**
 * This class represents the Game of Life. All rendering and computation happens in this 
 * class.
 */
class GameOfLife
{
    public:
        /**
         * Initalizes the renderer and the chunks according to predefined variables.
         */
        GameOfLife();

        /**
         * Returns the chunk by taking the position.
         */
        Chunk& getChunk(const Vector2l& pos);

        /**
         * Updates the chunks in parallel by using pthread library. Function will create
         * specified amount of threads to update chunks.The chunk load and delete procedure 
         * is given below:
         * 
         * When a cell borns near near the chunk the adjacent chunk is also loaded to memory.
         * 
         * When active cell count is zero and no other chunk points to the chunk it erease itself 
         * from memory.
         */
        void updateChunks(const unsigned short& threadCount=1);

        /**
         * Returns the rule for cell. Can only return 0, 1 or 2.
         * 
         * 0 : Cell will die
         * 1 : Cell will continue to live
         * 2 : A new cell will born
         */
        unsigned char rule(const unsigned int& adjCellAmount);

        /**
         * Does the render and computation. Window wont close until user hit close button.
         */
        void run();

    private:
        std::map<Vector2l, Chunk> chunks;

        Vector2l viewFramePosition;

        Vector2l viewFrameDimension;    

        sf::RenderWindow window;

        sf::RectangleShape cellRenderer;

        // It it hard coded because there can be at most 8 at least 0 asjacent cells 
        // around a cell. Total, 9 different number of cells.
        unsigned char rules[9]; 
};

#endif