odoo.define('supplier_visit.supplier_rating_widget', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');

    var SupplierRatingWidget = AbstractField.extend({
        template: 'supplier_visit_rating_widget',
        supportedFieldTypes: ['char'],

        init: function () {
            this._super.apply(this, arguments);
            this.rating = this._generateRandomRating();
        },

        _generateRandomRating: function () {
            // Generate a random rating between 1 and 5
            return Math.floor(Math.random() * 5) + 1;
        },

        _render: function () {
            this._super.apply(this, arguments);
            
            // Update the rating display
            var ratingContainer = this.$el.find('.rating-stars');
            var ratingText = this.$el.find('.rating-text');
            
            // Clear existing stars
            ratingContainer.empty();
            
            // Add stars based on rating
            for (var i = 1; i <= 5; i++) {
                var starClass = i <= this.rating ? 'fa-star' : 'fa-star-o';
                ratingContainer.append('<i class="fa ' + starClass + '"></i>');
            }
            
            // Update rating text
            ratingText.text(this.rating + ' out of 5 stars');
            
            // Add color based on rating
            ratingContainer.removeClass('text-warning text-success text-danger');
            if (this.rating >= 4) {
                ratingContainer.addClass('text-success');
            } else if (this.rating >= 3) {
                ratingContainer.addClass('text-warning');
            } else {
                ratingContainer.addClass('text-danger');
            }
        },

        _onClick: function (ev) {
            // Handle click events if needed
            this._super.apply(this, arguments);
        },
    });

    fieldRegistry.add('supplier_rating_widget', SupplierRatingWidget);

    return SupplierRatingWidget;
}); 