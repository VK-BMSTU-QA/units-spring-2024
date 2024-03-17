import { useProducts } from './useProducts';
import { renderHook } from '@testing-library/react';

describe('useProducts hook tests', () => {
    it('returns an array of products', () => {
        const { result } = renderHook(() => useProducts());
        expect(result.current).toHaveLength(4);
        for (let i = 0; i < 4; i++) {
            expect(result.current[i]).toHaveProperty('id');
            expect(result.current[i]).toHaveProperty('name');
            expect(result.current[i]).toHaveProperty('description');
            expect(result.current[i]).toHaveProperty('price');
            expect(result.current[i]).toHaveProperty('category');
        }
    });

    it('should return a list of products', () => {
        expect(useProducts()).toBeInstanceOf(Array);
    });
});
