import { useProducts } from '../useProducts';
import { Product } from '../../types';

describe('test useProducts function', () => {
    it('should return a list of products', () => {
        const prods = useProducts();
        expect(prods).toBeInstanceOf(Array);
        prods.forEach( (prod) => {
            expect(prod).toHaveProperty('id');
            expect(prod).toHaveProperty('name');
            expect(prod).toHaveProperty('description');
            expect(prod).toHaveProperty('price');
            expect(prod).toHaveProperty('category');
        });
    });
});