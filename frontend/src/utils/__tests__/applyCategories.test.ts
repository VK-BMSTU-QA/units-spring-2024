import { applyCategories } from '../applyCategories';

describe('test apply categories function', () => {
    it('should return the only one product with correct category', () => {
        expect(applyCategories([{id: 1, name: 'test-name', description: 'description', price:111,
            category: 'Электроника', imgUrl: 'some-url', priceSymbol: '$'}], ['Электроника'])).
        toStrictEqual([{id: 1, name: 'test-name', description: 'description', price:111,
            category: 'Электроника', imgUrl: 'some-url', priceSymbol: '$'}]);
    });

    it('should return 0 products', () => {
        expect(applyCategories([{id: 1, name: 'test-name', description: 'description', price:111,
            category: 'Электроника', imgUrl: 'some-url', priceSymbol: '$'}], ['Одежда'])).
        toStrictEqual([]);
    });

    it('should return all products, because categories.len == 0', () => {
        expect(applyCategories([{id: 1, name: 'test-name', description: 'description', price:111,
            category: 'Электроника', imgUrl: 'some-url', priceSymbol: '$'}], [])).
        toStrictEqual([{id: 1, name: 'test-name', description: 'description', price:111,
            category: 'Электроника', imgUrl: 'some-url', priceSymbol: '$'}]);
    });
});