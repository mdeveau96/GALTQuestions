<template>
    <div class="card">
        <img class="item-image" :src=product.image alt="item-photo"/>
        <h3>{{ product.name }}</h3>
        
        <h5 class="price">Price: ${{  product.price }}</h5>
        <p class="text-muted">{{ product.category }}</p>
        <div class="cart-total" v-if="product_total">
            <h3>In Cart</h3>
            <h4>{{ product_total }}</h4>
        </div>
        <div class="button-container">
            <button class="add-to-cart-button" @click=addToCart()>Add to Cart</button>
            <button class="remove-from-cart-button" @click=removeFromCart() v-if="product_total">Remove</button>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['product'],
        methods: {
            addToCart() {
                this.$store.commit('addToCart', this.product)
            },
            removeFromCart() {
                this.$store.commit('removeFromCart', this.product)
            }
        },
        computed: {
            product_total() {
                return this.$store.getters.productQuantity(this.product);
            }
        }
    };
</script>

<style>
    .card {
        width: 80%;
        margin: 10%;
        padding: 10px;
        border-radius: 5px;
        background-color: white;
        box-shadow: 0 0 5px gray;
        
        img.item-image {
            width: 100%;
        }

        h5.price {
            color: gray;
        }

        p.text-muted {
            color: gray;
        }
        .button-container {
            button {
                padding: 10px;
                background-color: rgb(79, 160, 187);
                border: none;
                color: white;
                font-weight: bold;
                font-size: 1.15rem;
                border-radius: 5px;
                margin: 0 5px 50px 5px;
                cursor: pointer;
            }
        }
    }

    @media (min-width: 500px) {
        .card {
            width: 350px;
            margin: 10px;
        }
    }
</style>