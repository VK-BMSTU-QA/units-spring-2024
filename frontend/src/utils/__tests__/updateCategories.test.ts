import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update categories function', () => {
    it('should add new category', () => {
      const categories: Category[] = ['0' as Category, '1' as Category, '2' as Category]
      const expected: Category[] = ['0' as Category, '1' as Category, '2' as Category, '3' as Category]
      expect(updateCategories(categories, '3' as Category)).toStrictEqual(expected)
    });
    it('should delete category', () => {
      const categories: Category[] = ['0' as Category, '1' as Category, '2' as Category]
      const expected: Category[] = ['1' as Category, '2' as Category] 
      expect(updateCategories(categories, categories[0])).toStrictEqual(expected)
    });
});
