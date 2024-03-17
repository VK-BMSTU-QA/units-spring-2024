import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

describe('test apply categories function', () => {
    const product: Product[] = [
        {
            id: 1,
            name: 'q',
            category: 'Одежда',
            description: 'q',
            imgUrl: '1',
            price: 100,
            priceSymbol: '₽',
        },
        {
            id: 1,
            name: 'q',
            category: 'Для дома',
            description: 'q',
            imgUrl: '1',
            price: 100,
            priceSymbol: '₽',
        },
        {
            id: 1,
            name: 'q',
            category: 'Электроника',
            description: 'q',
            imgUrl: '1',
            price: 100,
            priceSymbol: '₽',
        },
    ];
    const category: Category[] = ['Для дома', 'Одежда'];

    it('should return product with category from categories', () => {
        expect(applyCategories(product, category)).toStrictEqual([
            product[0],
            product[1],
        ]);
    })
    it('should return product with category from categories', () => {
        expect(applyCategories(product, ['Для дома'])).toStrictEqual([
            product[1],
        ]);
    });
    it('should return empty array', () => {
        expect(applyCategories([product[2]], category)).toStrictEqual([]);
    });
});
