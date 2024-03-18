import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

describe('test updateCategories function', () => {
    it.each([
        {
            currentCategories: ["Электроника" as Category],
            changedCategories: "New category" as Category,
            expected: ["Электроника" as Category, "New category" as Category]
        },
        {
            currentCategories: ["Электроника" as Category],
            changedCategories: "Электроника" as Category,
            expected: []
        },
        {
            currentCategories: ["Электроника" as Category, "Электроника2" as Category],
            changedCategories: "Электроника" as Category,
            expected: ["Электроника2" as Category]
        },
        {
            currentCategories: [],
            changedCategories: "Электроника" as Category,
            expected: ["Электроника" as Category]
        },
      ])('updateCategories($currentCategories, $categories)', ({currentCategories, changedCategories, expected}) => {
        expect(updateCategories(currentCategories, changedCategories)).toStrictEqual(expected);
      });
});
