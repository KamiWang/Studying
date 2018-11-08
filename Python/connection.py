import asyncio
import logging

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('10.10.10.11', 8888)

    for i in range(10):
        print(f'Send: {message!r}')
        writer.write(message.encode())

    input()
    # data = await reader.read(100)
    # print(f'Received: {data.decode()!r}')

    # print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client('你好!'))

def server():
    logging.basicConfig(level=logging.NOTSET)

    async def handle_echo(reader: asyncio.StreamReader, writer):
        while True:
            try:
                data = await reader.readuntil(b"\r\n\r\n")
                logging.debug("receive data length %d", len(data))
            except (EOFError, ConnectionResetError) as err:
                logging.debug(err)
                break

            try:
                message = data.decode()
            except UnicodeDecodeError:
                continue

            print(message)


    async def main():
        server = await asyncio.start_server(handle_echo, "10.10.10.11", 8888)

        addr = server.sockets[0].getsockname()
        print(addr) 

        async with server:
            await server.serve_forever()


    asyncio.run(main())
