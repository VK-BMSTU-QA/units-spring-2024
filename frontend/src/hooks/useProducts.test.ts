import { useProducts } from './useProducts';
import { renderHook } from '@testing-library/react';

describe('useProducts hook tests', () => {
    it('returns an array of products', () => {
        const { result } = renderHook(() => useProducts());
        expect(result.current).toHaveLength(4);
        expect(result.current[0]).toHaveProperty('id');
        expect(result.current[0]).toHaveProperty('name');
        expect(result.current[0]).toHaveProperty('description');
        expect(result.current[0]).toHaveProperty('price');
        expect(result.current[0]).toHaveProperty('category');
    });

    it('should return a list of products', () => {
        expect(useProducts()).toBeInstanceOf(Array);
    });
});
