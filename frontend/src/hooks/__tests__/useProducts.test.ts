import { useProducts } from "../useProducts";
import { renderHook } from '@testing-library/react';

describe("test useProduct function", () => {
    it('should return values with mandatory fields', () => {
        const { result } = renderHook(() => useProducts());

        result.current.forEach(product => {
            expect(product).toEqual(expect.objectContaining({
                id: expect.any(Number),
                name: expect.any(String),
                description: expect.any(String),
                price: expect.any(Number),
                category: expect.any(String)
            }));
        });
    })
});
