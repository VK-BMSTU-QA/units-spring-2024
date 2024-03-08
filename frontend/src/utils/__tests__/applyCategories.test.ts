import { applyCategories } from '../applyCategories';

describe('test get price function', () => {
    it('should return value with price symbol', () => {
        expect(applyCategories([{
            id: 1,
            name: 'P1',
            description: 'D1',
            price: 500000,
            priceSymbol: '$',
            category: 'Электроника'
        },{
            id: 2,
            name: 'P2',
            description: 'D2',
            price: 500000,
            priceSymbol: '₽',
            category: 'Для дома',
            imgUrl:'https://image.winudf.com/v2/image/b3JnLmthbGVlbS5iNHdvcmxkLm5pY2VzdW5zZXRmcmVlaW1hZ2VzX3NjcmVlbnNob3RzXzRfNGUyOTQ1MWQ/screen-4.jpg?fakeurl=1&type=.jpg'
        }, 
        {
            id: 3,
            name: 'P3',
            description: 'D3',
            price: -500000,
            category: 'Одежда',
            imgUrl:'https://image.winudf.com/v2/image/b3JnLmthbGVlbS5iNHdvcmxkLm5pY2VzdW5zZXRmcmVlaW1hZ2VzX3NjcmVlbnNob3RzXzRfNGUyOTQ1MWQ/screen-4.jpg?fakeurl=1&type=.jpg'
        }],[])).toStrictEqual([{
            id: 1,
            name: 'P1',
            description: 'D1',
            price: 500000,
            priceSymbol: '$',
            category: 'Электроника'
        },{
            id: 2,
            name: 'P2',
            description: 'D2',
            price: 500000,
            priceSymbol: '₽',
            category: 'Для дома',
            imgUrl:'https://image.winudf.com/v2/image/b3JnLmthbGVlbS5iNHdvcmxkLm5pY2VzdW5zZXRmcmVlaW1hZ2VzX3NjcmVlbnNob3RzXzRfNGUyOTQ1MWQ/screen-4.jpg?fakeurl=1&type=.jpg'
        }, 
        {
            id: 3,
            name: 'P3',
            description: 'D3',
            price: -500000,
            category: 'Одежда',
            imgUrl:'https://image.winudf.com/v2/image/b3JnLmthbGVlbS5iNHdvcmxkLm5pY2VzdW5zZXRmcmVlaW1hZ2VzX3NjcmVlbnNob3RzXzRfNGUyOTQ1MWQ/screen-4.jpg?fakeurl=1&type=.jpg'
        }]);
        expect(applyCategories([{
            id: 1,
            name: 'P1',
            description: 'D1',
            price: 500000,
            priceSymbol: '$',
            category: 'Электроника'
        },{
            id: 2,
            name: 'P2',
            description: 'D2',
            price: 500000,
            priceSymbol: '₽',
            category: 'Для дома',
            imgUrl:'https://image.winudf.com/v2/image/b3JnLmthbGVlbS5iNHdvcmxkLm5pY2VzdW5zZXRmcmVlaW1hZ2VzX3NjcmVlbnNob3RzXzRfNGUyOTQ1MWQ/screen-4.jpg?fakeurl=1&type=.jpg'
        }, 
        {
            id: 3,
            name: 'P3',
            description: 'D3',
            price: -500000,
            category: 'Одежда',
            imgUrl:'https://image.winudf.com/v2/image/b3JnLmthbGVlbS5iNHdvcmxkLm5pY2VzdW5zZXRmcmVlaW1hZ2VzX3NjcmVlbnNob3RzXzRfNGUyOTQ1MWQ/screen-4.jpg?fakeurl=1&type=.jpg'
        }], ['Для дома'])).toStrictEqual([{
            id: 2,
            name: 'P2',
            description: 'D2',
            price: 500000,
            priceSymbol: '₽',
            category: 'Для дома',
            imgUrl:'https://image.winudf.com/v2/image/b3JnLmthbGVlbS5iNHdvcmxkLm5pY2VzdW5zZXRmcmVlaW1hZ2VzX3NjcmVlbnNob3RzXzRfNGUyOTQ1MWQ/screen-4.jpg?fakeurl=1&type=.jpg'
        }]);
    });
});
