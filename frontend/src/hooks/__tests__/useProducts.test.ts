import { useProducts } from '../useProducts';
import { renderHook } from '@testing-library/react';

describe('test use products hook', () => {
    it('should return a valid list of products', () => {
        const { result } = renderHook(() => useProducts())
        
        expect(result.current).toBeInstanceOf(Array);
        
        expect(
            result.current.every(p => p.hasOwnProperty('id') && 
                p.hasOwnProperty('name') && 
                p.hasOwnProperty('description') && 
                p.hasOwnProperty('price') && 
                p.hasOwnProperty('category')
            )
        ).toBe(true);
    });
});
