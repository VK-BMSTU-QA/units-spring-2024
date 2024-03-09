import type { Category, Product } from '../../types';
import { applyCategories } from '../applyCategories';

describe('test get price function', () => {
    it('should return value with price symbol', () => {
        expect(applyCategories([
            {
                id: 1,
                name: "lol",
                description: "lol",
                price: 1,
                category: {
                    id: 1
                },
            }
        ],
        [
            {
                id: 1
            }
        ],
        )).toBe('100 ₽');
        expect(applyCategories()).toBe('325 $');
    });
});