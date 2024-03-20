import { PriceSymbol } from '../../types';
import { getPrice } from '../getPrice';

describe('test get price function', () => {
    it.each([
        [100, '₽', '100 ₽'],
        [325, '$', '325 $'],
        [0, '$', '0 $'],
        [0, '₽', '0 ₽'],
    ] as [number, PriceSymbol, string][])('should return value with price symbol', (value: number, symbol: PriceSymbol, expected: string) => {
        expect(getPrice(value, symbol)).toBe(expected);
    });
});
