import { applyCategories } from '../applyCategories';
import { Product } from '../../types/Product';
import { Category } from '../../types/Category';

const testProducts: Product[] = [
    {
        id: 1,
        name: '1',
        description: '1',
        price: 1,
        category: 'Электроника'
    },
    {
        id: 2,
        name: '2',
        description: '2',
        price: 2,
        category: 'Для дома',
    },
    {
        id: 3,
        name: '3',
        description: '3',
        price: 3,
        category:  'Одежда',
    }
]

describe('test applyCategories function', () => {
    it('should return a list of products with the specified categories', () => {
        expect(applyCategories(testProducts, ["Электроника"])).toStrictEqual([testProducts[0]]);
        expect(applyCategories(testProducts, ["Одежда"])).toStrictEqual([testProducts[2]]);
        expect(applyCategories(testProducts, ["Для дома"])).toStrictEqual([testProducts[1]]);
        expect(applyCategories(testProducts, ["Одежда", "Для дома"])).toStrictEqual([testProducts[1], testProducts[2]]);
    });
    it('should return a list of all original products', () => {
        expect(applyCategories(testProducts, [])).toStrictEqual(testProducts);
    });
});
