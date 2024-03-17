import { getPrice } from '../getPrice';

describe('test get price function', () => {
    it('should return value with price symbol', () => {
        expect(getPrice(100, '₽')).toBe('100 ₽');
        expect(getPrice(325, '$')).toBe('325 $');
    });

    it('should return 0 with price symbol', () => {
        expect(getPrice(0, '$')).toBe('0 $');
    });

    it('should return negative value with price symbol', () => {
        expect(getPrice(-325, '$')).toBe('-325 $');
    });

    it('should return float value with price symbol', () => {
        expect(getPrice(0.999, '$')).toBe('0,999 $');
    });
});
