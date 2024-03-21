import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test apply categories function', () => {
    it('should return filtered products with needed categories', () => {
        const testCategories: Product[] = [
            {
                id: 1,
                name: 'test1',
                description: 'test1',
                price: 2,
                priceSymbol: '$',
                imgUrl: '',
                category: 'Электроника',
            },
            {
                id: 2,
                name: 'test2',
                description: 'test2',
                price: 2,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',
            },
            {
                id: 3,
                name: 'test3',
                description: 'test3',
                price: 3,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Одежда',
            },
        ];

        expect(applyCategories(testCategories, ['Электроника'])).toStrictEqual(
            testCategories.slice(0, 1)
        );
        expect(applyCategories(testCategories.slice(0, 2), [])).toStrictEqual(
            testCategories.slice(0, 2)
        );
    });
});
