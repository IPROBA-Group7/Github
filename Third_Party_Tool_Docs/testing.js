//Changes for testing n8n workflow
'use strict';

/**
 * Calculates the total price including tax.
 * @param {number} price
 * @param {number} taxRate
 * @returns {number}
 */
function calculateTotal(price, taxRate = 0.2) {
    if (typeof price !== 'number' || price < 0) {
        throw new Error('Invalid price');
    }
    if (typeof taxRate !== 'number' || taxRate < 0) {
        throw new Error('Invalid tax rate');
    }

    return Number((price * (1 + taxRate)).toFixed(2));
}

module.exports = { calculateTotal };
