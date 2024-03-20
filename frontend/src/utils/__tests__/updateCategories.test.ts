import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';


describe('updateCategories', () => {
    const currentCategories: Category[] = ['Электроника', 'Для дома'];
    
    it('should handle empty currentCategories', () => {
        const changedCategory = 'Одежда';
        expect(updateCategories([], changedCategory)).toEqual(['Одежда']);
      });

    it('should remove category if it exists in currentCategories', () => {
      const changedCategory = 'Для дома';
      expect(updateCategories(currentCategories, changedCategory)).toEqual(['Электроника']);
    });
  
    it('should add category if it does not exist in currentCategories', () => {
      const changedCategory = 'Одежда';
      expect(updateCategories(currentCategories, changedCategory)).toEqual(['Электроника', 'Для дома', 'Одежда']);
    });
   
  });