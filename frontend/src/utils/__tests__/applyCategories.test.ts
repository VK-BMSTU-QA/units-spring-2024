import type { Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test applyCategories', () => {
    const clothes: Product[] = [
        {
            id: 1,
            name: 'Dress',
            description: 'test',
            price: 5000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
        {
            id: 2,
            name: 'Coat',
            description: 'test',
            price: 20000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
    ];

    const productsForHome: Product[] = [
        {
            id: 3,
            name: 'Desk',
            description: 'test',
            price: 300,
            priceSymbol: '$',
            category: 'Для дома',
        },
    ];

    const electronics: Product[] = [
        {
            id: 4,
            name: 'TV',
            description: 'test',
            price: 1500,
            priceSymbol: '$',
            category: 'Электроника',
        },
    ];

    it('should do nothing', () => {
        expect(applyCategories(productsForHome, [])).toEqual(productsForHome);
    });

    const allProducts: Product[] = [
        ...clothes,
        ...productsForHome,
        ...electronics,
    ];

    it('should filter clothes', () => {
        expect(applyCategories(allProducts, ['Одежда'])).toEqual(clothes);
    });

    it('should filter products for home', () => {
        expect(applyCategories(allProducts, ['Для дома'])).toEqual(
            productsForHome
        );
    });

    it('should filter electronics', () => {
        expect(applyCategories(allProducts, ['Электроника'])).toEqual(
            electronics
        );
    });
});
