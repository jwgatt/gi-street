<template>
    <div class="container">
        <div class="row ">
            <div class="col-md-16">
                <h1 class="title">Success</h1>
                <h2 class="subtitle">Thank you for your order!</h2>
            </div>
        </div>
    </div>
</template>
<script>
export default{
    name:"Success",
    mounted(){
        document.title = "Success";
    }
}
</script>