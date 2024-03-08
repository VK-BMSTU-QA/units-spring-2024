import { useProducts } from './useProducts';

describe('useProducts hook tests', () => {
    it('should return array of products', () => {
        const products = useProducts();

        expect(Array.isArray(products)).toBe(true);

        expect(products).toHaveLength(4);

        products.forEach((product) => {
            expect(product).toHaveProperty('id');
            expect(product).toHaveProperty('name');
            expect(product).toHaveProperty('description');
            expect(product).toHaveProperty('price');
            expect(product).toHaveProperty('priceSymbol');
            expect(product).toHaveProperty('category');
            expect(product).toHaveProperty('imgUrl');
        });
    });
});
