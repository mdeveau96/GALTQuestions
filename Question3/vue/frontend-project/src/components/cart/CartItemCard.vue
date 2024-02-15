<template>
    <div class="card-item-card">
        <div class="header">
            <img class="item-image" :src=product.image alt="item-photo"/>
            <h3>{{ product.name }}</h3>
            <h4>In cart: {{ product.quantity }}</h4>
            <h4>Total Cost: {{ item_cost }}</h4>
        </div>
    </div>
</template>

<script>
export default {
    props: ['product'],
    computed: {
        item_cost() {
            return this.product.price * this.product.quantity;
        }
    }
};
</script>

<style lang="scss">
.card-item-card {
    width: 90%;
    margin: 5%;
    background-color: white;
    box-shadow: 0 0 5px gray;
    border-radius: 5px;
    padding: 10px;
    text-align: left;

    .header {
        display: flex;
        justify-content: space-around;
    }

    img.item-image {
            width: 100%;
        }
}
</style>