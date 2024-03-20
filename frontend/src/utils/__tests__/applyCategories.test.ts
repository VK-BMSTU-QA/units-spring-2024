import { applyCategories } from '../applyCategories';
import { useProducts } from '../../hooks';

const products = useProducts();

describe('test apply categories function', () => {
    it('should return an empty list of products with empty parameters', () => {
        expect(applyCategories([], [])).toStrictEqual([]);
    });

    it('should return all products with an empty list categories', () => {
        expect(applyCategories([
            {
                id: 1,
                name: '',
                description: '',
                price: 1000,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',

            },
            {
                id: 2,
                name: '',
                description: '',
                price: 999999,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',

            },
        ], [])).toStrictEqual([
            {
                id: 1,
                name: '',
                description: '',
                price: 1000,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',

            },
            {
                id: 2,
                name: '',
                description: '',
                price: 999999,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',

            },
        ]);
    });

    it('should return all products whose categories are contained in the transmitted list', () => {
        expect(applyCategories([
            {
                id: 1,
                name: '',
                description: '',
                price: 1000,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',
    
            },
            {
                id: 2,
                name: '',
                description: '',
                price: 999999,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Электроника',
    
            },
        ], ['Одежда', 'Для дома'])).toStrictEqual([
            {
                id: 1,
                name: '',
                description: '',
                price: 1000,
                priceSymbol: '₽',
                imgUrl: '',
                category: 'Для дома',
            },
        ]);
    });
});
