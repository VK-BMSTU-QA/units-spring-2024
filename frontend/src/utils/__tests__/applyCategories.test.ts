import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';
import { useProducts } from '../../hooks';

const products = useProducts();

describe('test apply categories function', () => {
    it('should return a categories array', () => {
        expect(applyCategories(products, [])).toBe(products);
        expect(applyCategories(products, ['Электроника'])).toEqual([
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ]);
    });
});
