import { useProducts } from '../useProducts';

describe('test useProducts function', () => {
    it('should return a list of products', () => {
        expect(useProducts()).toBeInstanceOf(Array);
    });
});