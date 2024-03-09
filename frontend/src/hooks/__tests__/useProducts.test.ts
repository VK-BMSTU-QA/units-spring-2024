import { useProducts } from '../useProducts';

describe('useProducts hook', () => {
    it('should return non-empty array of products', () => {
        const products = useProducts();
        expect(products).toBeDefined();
        expect(products.length).toBeGreaterThan(0);
    });

    it('should return array of products with correct properties', () => {
        const products = useProducts();
        products.forEach(product => {
            expect(product).toHaveProperty('id');
            expect(product).toHaveProperty('name');
            expect(product).toHaveProperty('description');
            expect(product).toHaveProperty('price');
            expect(product).toHaveProperty('category');
        });
    });

    it('should return array of products with correct length', () => {
        const products = useProducts();
        expect(products.length).toBe(4);
    });
});
