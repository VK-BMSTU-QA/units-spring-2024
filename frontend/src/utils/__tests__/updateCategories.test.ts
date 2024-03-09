import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update сategories function', () => {
  it('should remove the category if it already exists in the list', () => {
    const currentCategories: Category[] = ['Электроника', 'Для дома', 'Одежда'];
    const changedCategory = 'Для дома';

    const updatedCategories = updateCategories(currentCategories, changedCategory);

    expect(updatedCategories).toEqual(['Электроника', 'Одежда']);
  });

  it('should add the category if it does not exist in the list', () => {
    const currentCategories: Category[] = ['Электроника', 'Для дома'];
    const changedCategory = 'Одежда';

    const updatedCategories = updateCategories(currentCategories, changedCategory);

    expect(updatedCategories).toEqual(['Электроника', 'Для дома', 'Одежда']);
  });
});
