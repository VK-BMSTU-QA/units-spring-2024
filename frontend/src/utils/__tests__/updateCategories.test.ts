import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

describe('test update categories function', () => {
    it('should remove category from array if presents', () => {
        const categories = ['Электроника' as Category, 'Для дома' as Category];
        const selectedCategory = 'Электроника' as Category;
        const result = updateCategories(categories, selectedCategory);
        expect(result).toHaveLength(1);
        expect(result).toContain(categories[1]);
    });
    it('should add category to array if not presents', () => {
        const categories = ['Для дома' as Category];
        const selectedCategory = 'Электроника' as Category;
        const result = updateCategories(categories, selectedCategory);
        expect(result).toHaveLength(2);
        expect(result).toContain(categories[0]);
        expect(result).toContain(selectedCategory);
    });
});
