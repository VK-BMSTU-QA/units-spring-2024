import { renderHook } from '@testing-library/react-hooks';
import { useProducts } from '../useProducts';

describe('useProducts', () => {
  it('returns an array of products', () => {
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