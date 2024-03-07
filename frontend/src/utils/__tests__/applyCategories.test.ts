import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';

const PRODUCTS: Product[] = [
    {
        id: 1,
        name: 'Product 1',
        description: 'Description 1',
        price: 100,
        category: 'Электроника',
    },
    {
        id: 2,
        name: 'Product 2',
        description: 'Description 2',
        price: 200,
        category: 'Для дома',
    },
    {
        id: 3,
        name: 'Product 3',
        description: 'Description 3',
        price: 150,
        category: 'Одежда',
    },
];

describe('applyCategories', () => {
    test('should return all products if no categories are provided', () => {
        const filteredPRODUCTS = applyCategories(PRODUCTS, []);
        expect(filteredPRODUCTS).toEqual(PRODUCTS);
    });

    test('should filter products based on provided categories', () => {
        const categories: Category[] = ['Электроника', 'Для дома'];
        const filteredPRODUCTS = applyCategories(PRODUCTS, categories);
        expect(filteredPRODUCTS).toEqual([
            {
                id: 1,
                name: 'Product 1',
                description: 'Description 1',
                price: 100,
                category: 'Электроника',
            },
            {
                id: 2,
                name: 'Product 2',
                description: 'Description 2',
                price: 200,
                category: 'Для дома',
            },
        ]);
    });
});
