const gulp = require('gulp');
const sass = require('gulp-sass');

// [Style] src and desitnation
const sassSrc = '../static/scss';
const sassDest = '../static/css/';

// [IMG] Image processing
gulp.task('sass', function() {
    return gulp.src(`${sassSrc}/*.scss`)
    .pipe(sass())
    .pipe(gulp.dest(sassDest));
});

