import { applyCategories } from '../applyCategories';
import {Category, Product} from "../../types";

const testProducts: Product[] = [
    {
        id: 1,
        name: 'test-name',
        description: 'description',
        price:111,
        category: 'Электроника',
        imgUrl: 'some-url',
        priceSymbol: '$'
    },
];


describe('test apply categories function', () => {
    it('should return the only one product with correct category', () => {
        expect(applyCategories(testProducts, ['Электроника'])).
        toStrictEqual(testProducts);
    });

    it('should return 0 products', () => {
        expect(applyCategories(testProducts, ['Одежда'])).
        toStrictEqual([]);
    });

    it('should return all products, because categories.len == 0', () => {
        expect(applyCategories(testProducts, [])).
        toStrictEqual(testProducts);
    });
});