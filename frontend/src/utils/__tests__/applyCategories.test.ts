import type { Category, Product } from '../../types';

import { applyCategories } from '../applyCategories';

const products: Product[] = [
    {
        id: 0,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 999,
        category: 'Электроника',
    },
    {
        id: 1,
        name: 'Костюм гуся',
        description: 'Запускаем гуся, работяги',
        price: 1000,
        category: 'Одежда',
    },
];

describe('test applyCategories function', () => {
    it('should return products filtered by category ', () => {
        const categories: Category[] = ['Электроника'];
        expect(applyCategories(products, categories)).toStrictEqual(
            products.filter((product) => categories.includes(product.category))
        );
    });
});

describe('test applyCategories function', () => {
    it('should return unfiltered products', () => {
        expect(applyCategories(products, [])).toBe(products);
    });
});
