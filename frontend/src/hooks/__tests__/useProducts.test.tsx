import { useProducts } from '../useProducts';

describe('test useProducts function', () => {
    it('should return a list of products', () => {
        expect(useProducts()).toBeInstanceOf(Array);
    });

    it('mandatory properties for each product should be defined', () => {
        const products = useProducts();
        products.forEach((product) => {
            expect(product.id).toBeDefined();
            expect(product.name).toBeDefined();
            expect(product.description).toBeDefined();
            expect(product.price).toBeDefined();
            expect(product.category).toBeDefined();
        });
      });
});
