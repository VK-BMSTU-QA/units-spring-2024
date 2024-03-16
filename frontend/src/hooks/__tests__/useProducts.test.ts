import { Product } from '../../types';
import { useProducts } from '../useProducts';

describe('test use products function', () => {
    const products: Product = {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 999,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: '/iphone.png',
    };

    it('should contain all properties', () => {
        const res = useProducts()[0];
        for (const prop in products) {
            expect(res.hasOwnProperty(prop)).toBeTruthy();
        }
    });
});
