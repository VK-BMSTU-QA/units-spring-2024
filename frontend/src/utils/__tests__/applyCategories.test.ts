import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

describe('test applyCategories function', () => {
    const products: Product[] = [
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
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
    ];

    const categories: Category[] = ['Электроника'];

    it('should return products with filter categories', () => {
        expect(applyCategories(products, categories)).toEqual([
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
        ]);
    });

    it('should return full products, categories empty', () => {
        expect(applyCategories(products, [])).toEqual(products);
    });
});
