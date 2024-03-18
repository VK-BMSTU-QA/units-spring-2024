import { useProducts } from '../useProducts'
import type { Product } from '../../types';
import exp from 'constants';
import { string } from 'yargs';


describe('Use products test', () => {
  it('should always return an array of the objects', () => {
    const expected: Product[] = [
      expect.objectContaining({
        id: expect.any(Number),
        name: expect.any(String),
        description: expect.any(String),
        price: expect.any(Number),
        category: expect.any(String),
      }),
    ]
      const result = useProducts();
      expect(result).toEqual(
        expect.arrayContaining(expected),
      );
  });
});
