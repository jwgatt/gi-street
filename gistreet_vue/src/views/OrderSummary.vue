<template>
    <div class="box mb-4">
        <h3 class="is-size-4">Order #{{ order.id }}</h3>

        <h4 class="is-size-5">Order Date: {{ order.date }}</h4>

        <h3 class="is-size-4">Products</h3>

        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Quantity</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in order.items" :key="item.product.id">
                    <td>{{ item.name }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>{{ item.price }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>

export default {
    name: "OrderSummary",
    props: {
        order: Object
    },
    methods:{
        getItemTotal(item){
            return item.quantity * item.price
        },
        orderTotalLength(order){
            return this.order.items.length
        }
    }
}

</script>