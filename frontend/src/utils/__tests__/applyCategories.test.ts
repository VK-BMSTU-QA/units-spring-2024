import { Categories } from '../../components';
import type { Category, Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test apply categories function', () => {
    it('should return products with selected categories', () => {
        const products: Product[] = [
            {
                id: 1,
                category: 'Для дома',
                name: "asd",
                description: "asd",
                price: 123,
            },
            {
                id: 2,
                category: 'Одежда',
                name: "asdasd",
                description: "asdasd",
                price: 123,
            },
        ];
        const categories: Category[] = [
            'Для дома'
        ]
        expect(applyCategories(products, ['Для дома'])).toEqual([products[0]]);
        // expect(applyCategories(products, [])).toBe(products);
    });
    it('should return same products without selected categ', () => {
        const products: Product[] = [
            {
                id: 1,
                category: 'Для дома',
                name: "asd",
                description: "asd",
                price: 123,
            },
            {
                id: 2,
                category: 'Одежда',
                name: "asdasd",
                description: "asdasd",
                price: 123,
            },
        ];

        expect(applyCategories(products, [])).toBe(products);
    });
});