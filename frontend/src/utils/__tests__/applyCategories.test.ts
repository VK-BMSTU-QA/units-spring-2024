import { applyCategories } from '../applyCategories';
import { useProducts } from '../../hooks';

const products = useProducts();

describe('test apply categories function', () => {
    it('should return value needs products', () => {
        expect(applyCategories([], [])).toStrictEqual([]);

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
