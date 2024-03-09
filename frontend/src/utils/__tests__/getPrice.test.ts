import { getPrice } from '../getPrice';

describe('test get price function', () => {
    it('should return value with price symbol', () => {
        expect(getPrice(100, '₽')).toBe('100 ₽');
        expect(getPrice(325, '$')).toBe('325 $');
        expect(getPrice(325.1, '$')).toBe('325,1 $');
        expect(getPrice(325.123, '$')).toBe('325,123 $');
    });
});
