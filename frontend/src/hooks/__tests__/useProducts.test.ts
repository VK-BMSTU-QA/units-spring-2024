import { renderHook } from '@testing-library/react';
import { Product } from '../../types';
import { useProducts } from '../useProducts';

describe('test useProducts', () => {
    it('should return correct products', () => {
        const { result } = renderHook(() => useProducts());

        const expectedFields = ['id', 'name', 'description', 'price', 'category'];

        result.current.forEach(product => {
            expect(product).toEqual(expect.objectContaining({
                id: expect.any(Number),
                name: expect.any(String),
                description: expect.any(String),
                price: expect.any(Number),
                category: expect.any(String)
            }));
        });
    });
});
