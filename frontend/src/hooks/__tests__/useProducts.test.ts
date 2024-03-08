import { renderHook } from '@testing-library/react';
import { useProducts } from '../useProducts'; // replace with the correct path
import type { Product } from '../../types';

describe('useProducts', () => {
  it('returns an array of products', () => {
    const { result } = renderHook(() => useProducts());

    expect(result.current).toBeInstanceOf(Array);
    expect(result.current.length).toBeGreaterThan(0);
  });

  it('each product has the required properties', () => {
    const { result } = renderHook(() => useProducts());

    result.current.forEach((product: Product) => {
      expect(product).toHaveProperty('id');
      expect(product).toHaveProperty('name');
      expect(product).toHaveProperty('description');
      expect(product).toHaveProperty('price');
      expect(product).toHaveProperty('category');

      if (product.imgUrl) {
        expect(product).toHaveProperty('imgUrl');
      }

      if (product.priceSymbol) {
        expect(product).toHaveProperty('priceSymbol');
      }
    });
  });
});
