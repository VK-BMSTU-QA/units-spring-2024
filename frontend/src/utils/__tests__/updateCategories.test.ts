import { updateCategories } from '../updateCategories';

describe('test update categories', () => {
    it('should return updated categories', () => {
        expect(
            updateCategories(['Для дома', 'Одежда'], 'Электроника')
        ).toStrictEqual(['Для дома', 'Одежда', 'Электроника']);
        expect(
            updateCategories(['Для дома', 'Одежда'], 'Одежда')
        ).toStrictEqual(['Для дома']);
    });
});
