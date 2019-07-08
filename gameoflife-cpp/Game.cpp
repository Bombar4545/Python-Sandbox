/**
 * Author: Ufuk Bombar
 * Date: Jul 6 2019
 */

// Includes
#include "Game.hpp"
#include <vector>
#include <map>
#include <SFML/Graphics.hpp>

/**
 * Initalizes the renderer and the chunks according to predefined variables.
 */
GameOfLife::GameOfLife()
:   
    // Initializes view frame dimension.
    viewFrameDimension(Vector2l(
        VIEW_FRAME_DIMENSION_CELL_WIDTH, 
        VIEW_FRAME_DIMENSION_CELL_HEIGHT)),

    // Sets view frame position to zero.
    viewFramePosition({0, 0}), 

    // Creates the renderer.
    window(sf::RenderWindow(
        sf::VideoMode(
            VIEW_FRAME_DIMENSION_CELL_WIDTH * CELL_SIZE_PIXEL, 
            VIEW_FRAME_DIMENSION_CELL_HEIGHT * CELL_SIZE_PIXEL), 
            WINDOW_TITLE)),
    
    // Sets the rules of life.
    rules({CELL_RULES})
{
    // Sets the properties of cell renderer.
    cellRenderer.setScale(sf::Vector2f(CELL_SIZE_PIXEL, CELL_SIZE_PIXEL));
    cellRenderer.setFillColor(sf::Color::Green);
    cellRenderer.setOutlineColor(sf::Color::Magenta);
    cellRenderer.setOutlineThickness(1.0f);
}

/**
 * Returns the chunk by taking the position. Function expects a positive 
 * and less than 9.
 */
Chunk& 
GameOfLife::getChunk(const Vector2l& pos)
{
    return chunks[pos];
}

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
void 
GameOfLife::updateChunks(const unsigned short& threadCount)
{
    // ==NOT IMPLEMENTED YET==
}

/**
 * Returns the rule for cell. Can only return 0, 1 or 2.
 * 
 * 0 : Cell will die
 * 1 : Cell will continue to live
 * 2 : A new cell will born
 */
unsigned char 
GameOfLife::rule(const unsigned int& adjCellAmount)
{
    return rules[adjCellAmount];
}

/**
 * Does the render and computation. Window wont close until user hit close button.
 */
void 
GameOfLife::run()
{
    sf::Event event;

    while (window.isOpen())
    {        
        // Check for window events. Mouse and others will be taken here.
        while (window.pollEvent(event))
            if (event.type == sf::Event::Closed)
                window.close();

        window.clear();

        // Cells that are in the view frame will be drawn here.

        // ==NOT IMPLEMENTED YET==
        
        window.display();
    }
}

/**
 * This function is necessary for hashing.
 */
bool Vector2l::operator<(const Vector2l& vec) const
{
    // same as comparing the magnituted, but this method prevents overflow.
    return (x + vec.x) * (x - vec.x) < (vec.y + y) * (vec.y - y);
}

Vector2l::Vector2l(long x, long y)
: x(x), y(y)
{ }

/**
 * Initializes the chunk variables: 'activelist', 'renderlist', 'position'.
 */
Chunk::Chunk(const Vector2l& pos)
: 
    activelist(std::vector<Cell>()),

    position(pos)
{
    clearRenderList();
}

/**
 * Clears the render list, initializes each cell to dead for fresh start.
 */
void Chunk::clearRenderList()
{
    for (unsigned short i = 0; i < CHUNK_WIDTH; i++)
        for (unsigned short j = 0; j < CHUNK_WIDTH; j++)
            renderlist[i][j] = false;
}

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
void 
Chunk::update(GameOfLife& game)
{
    // ==NOT IMPLEMENTED YET==
}

/**
 * Takes x and t position returns if the corresponding cell is alive or not
 */
bool 
Chunk::isAlive(const Vector2l& pos)
{
    return renderlist[pos.y][pos.x];
}
