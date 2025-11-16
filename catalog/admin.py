from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Product, Cart, CartItem, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    exclude = ('slug',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_available', 'featured')
    search_fields = ('name',)
    list_filter = ('category', 'color', 'material', 'is_available', 'featured')
    list_editable = ('price', 'stock')
    prepopulated_fields = {'slug': ('name',)}

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'updated_at')
    list_filter = ('user',)
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'total_amount', 'created_at')
    search_fields = ('order_number', 'user__username')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]

#class CustomUserProfileInline(admin.StackedInline):
    #model = CustomUserProfile
    #can_delete = False
    #verbose_name_plural = 'Profile'

#class CityFilter(admin.SimpleListFilter):
    #title = 'city'
    #parameter_name = 'city'

    #def lookups(self, request, model_admin):
        #cities = set(CustomUserProfile.objects.values_list('city', flat=True))
        #return [(c, c) for c in cities if c]

    #def queryset(self, request, queryset):
        #if self.value():
            #return queryset.filter(custom_profile__city=self.value())
        #return queryset

#class CustomUserAdmin(admin.ModelAdmin):
    #inlines = (CustomUserProfileInline,)
    #list_display = ('username', 'email', 'get_full_name', 'is_staff')
    #search_fields = ('username', 'email', 'custom_profile__first_name', 'custom_profile__last_name', 'custom_profile__phone')
    #list_filter = (CityFilter,)

    def get_full_name(self, obj):
        if hasattr(obj, 'custom_profile'):
            return obj.custom_profile.get_full_name()
        return ''
    get_full_name.short_description = 'Full Name'

admin.site.unregister(User)
#admin.site.register(User, CustomUserAdmin)
