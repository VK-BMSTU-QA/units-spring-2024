import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test apply categories function', () => {
    it('should return the same products when no categories are provided', () => {
        const products: Product[] = [
            {
                id: 1,
                name: 'Product 1',
                description: 'Description 1',
                price: 1000,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',
            },
            {
                id: 2,
                name: 'Product 2',
                description: 'Description 2',
                price: 999999,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',
            },
        ];

        const result = applyCategories(products, []);

        expect(result).toEqual(products);
    });

    it('should filter products by specified categories', () => {
        const products: Product[] = [
            {
                id: 1,
                name: 'Product 1',
                description: 'Description 1',
                price: 1000,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',
            },
            {
                id: 2,
                name: 'Product 2',
                description: 'Description 2',
                price: 999999,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Электроника',
            },
        ];

        const result = applyCategories(products, ['Для дома']);

        expect(result).toEqual([
            {
                id: 1,
                name: 'Product 1',
                description: 'Description 1',
                price: 1000,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',
            },
        ]);
    });
});
