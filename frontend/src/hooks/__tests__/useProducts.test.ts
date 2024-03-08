import { useProducts } from '../useProducts';

describe('test useProducts', () => {
    it('should return an array of products', () => {
        const products = useProducts();

        expect(products).toBeInstanceOf(Array);
        expect(products.length).toBeGreaterThan(0);
    });

    it('should have valid properties', () => {
        const products = useProducts();

        products.forEach((product) => {
            expect(typeof product.id).toBe('number');
            expect(typeof product.name).toBe('string');
            expect(typeof product.description).toBe('string');
            expect(typeof product.price).toBe('number');
            expect(typeof product.category).toBe('string');
        });
    });
});
