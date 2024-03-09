import { updateCategories } from '../updateCategories';
import { Category } from '../../types/Category';

const testCategory: Category[] = [
    "Для дома",
    "Электроника"
]

describe('test updateCategories function', () => {
    it('should return a list of categories without the specified', () => {
        expect(updateCategories(testCategory, "Электроника")).toStrictEqual(["Для дома"]);
        expect(updateCategories(testCategory, "Для дома")).toStrictEqual(["Электроника"]);
    })
    it('should return a list of categories with the specified', () => {
        expect(updateCategories(testCategory, "Одежда")).toStrictEqual(["Для дома", "Электроника", "Одежда"]);
    })
})