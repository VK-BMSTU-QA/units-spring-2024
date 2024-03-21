import { applyCategories } from '../applyCategories';
import type { Product } from '../../types';

const testData: Product[] = [
    {id: 1, name: 'Aspire ES 15', description: 'Ноутбук', price: 100, category: 'Электроника'},
    {id: 2, name: 'Samsung Galaxy S9+', description: 'Телефон', price: 50, category: 'Электроника'},
    {id: 3, name: 'Dyson HZ', description: 'Пылесос', price: 200, category: 'Для дома'},
]

describe('test apply categories function', () => {
    it('should filter products with applicable categories', () => {
        expect(applyCategories(
            testData,
            ['Электроника'])
        ).toStrictEqual(
            [testData[0], testData[1]]
        );
        expect(applyCategories(
            testData,
            ['Для дома'])
        ).toStrictEqual(
            [testData[2]]
        );
        expect(applyCategories(
            testData,
            ['Одежда'])
        ).toStrictEqual(
            []
        );
    });
    it('should return all products if no categories are provided', () => {
        expect(applyCategories(
            testData,
            [])
        ).toStrictEqual(
            testData
        );
    });
});
