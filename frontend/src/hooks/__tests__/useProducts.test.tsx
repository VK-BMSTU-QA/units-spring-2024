import { useProducts } from '../useProducts';
import type { Product } from '../../types';

describe('test use products hook', () => {
    test('should return an array of products with correct structure', () => {
        const products = useProducts();

        expect(products).toBeInstanceOf(Array);

        products.forEach((product) => {
            expect(product).toHaveProperty('id');
            expect(product).toHaveProperty('name');
            expect(product).toHaveProperty('description');
            expect(product).toHaveProperty('price');
            expect(product).toHaveProperty('category');
        });
    });
});